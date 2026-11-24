// Read the author's published data as an AST. Never load or execute the source scripts.
const { readFileSync } = require("node:fs");
const { parse } = require("acorn");

function literal(node) {
  if (node.type === "Literal" && !node.regex && node.bigint === undefined) return node.value;
  if (node.type === "TemplateLiteral" && node.expressions.length === 0) return node.quasis[0].value.cooked;
  if (node.type === "ArrayExpression") return node.elements.map(literal);
  if (node.type === "ObjectExpression") {
    const entries = new Map();
    for (const property of node.properties) {
      if (property.type !== "Property" || property.computed || property.kind !== "init" || property.method) {
        throw new Error("Reading bank contains a nonliteral property");
      }
      const field = property.key.name ?? property.key.value;
      if (entries.has(field)) throw new Error("Reading bank contains a duplicate property");
      entries.set(field, literal(property.value));
    }
    return Object.fromEntries(entries);
  }
  throw new Error("Expected a static Reading data literal");
}

function extract(source) {
  const tree = parse(source, { ecmaVersion: 2024, locations: true });
  const body = tree.body[0]?.expression?.callee?.body?.body;
  if (!body || tree.body.length !== 1) throw new Error("Unsupported author source layout");
  const arrays = [];
  for (const statement of body) {
    if (statement.type === "VariableDeclaration") {
      for (const declaration of statement.declarations) {
        if (declaration.init?.type === "ArrayExpression") arrays.push([declaration.id.name, declaration.init]);
      }
    }
    const object = statement.expression?.callee?.object;
    if (object?.type === "ArrayExpression") arrays.push(["inline", object]);
  }
  return arrays.flatMap(([section, array]) => array.elements.map(node => {
    const children = node.properties?.find(property =>
      ["items", "questions"].includes(property.key?.name ?? property.key?.value));
    const questionLines = children?.value.elements?.map(question => question.loc.start.line) ?? [node.loc.start.line];
    return { section, questionLines, value: literal(node) };
  }));
}

const verifiedFiles = JSON.parse(readFileSync(0, "utf8"));
process.stdout.write(JSON.stringify(Object.fromEntries(
  Object.entries(verifiedFiles).map(([file, source]) => [file, extract(source)]),
)));
