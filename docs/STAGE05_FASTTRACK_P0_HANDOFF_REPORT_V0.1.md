# Stage05 Fast Track — Bàn giao P0 và Listening Lab V0.1

Ngày 22/11/2026 (Asia/Saigon). Nhánh `development/fasttrack-48h-preview` tiếp tục từ `ecfe55abd728c958a48c948c88cc6b5919c0629f`. Tham chiếu [chỉ đạo PO V0.2](STAGE05_FASTTRACK_PO_RIGHTS_AND_EXECUTION_PRIORITY_V0.2.md) và [Issue #7](https://github.com/hieupham03/TOEIC-Learning-App/issues/7).

## Bản bàn giao hai máy và bản lab

- **Hai máy** dùng `TOEIC-P0-0.2.1.apk` trong gói cục bộ, package `vn.toeiclearning.alpha`, versionCode 3, min API 26, target API 36. Gói có checksum, [hướng dẫn và checklist](STAGE05_FASTTRACK_TWO_PHONE_HANDOFF_V0.1.md) và phiếu ghi lỗi. Listening Part 1–4 dùng bốn WAV tự tạo. Reading Part 5–7 dùng fixture hiện hữu. Lựa chọn giữ trong RAM của phiên.
- **Lab trên máy nội bộ** dùng build type `localPreview`, package `vn.toeiclearning.alpha.listeningpreview`. Mở **Listening DEMO → Mở Part 3 DEMO tiếng Anh**. Một MP3 cho Q32–34, lựa chọn chỉ hiện trong màn hình, không kèm đáp án và không chấm. Người xem thấy nhãn **DEMO / CHƯA QA**.
- **Play** dùng AAB synthetic, cùng package và versionCode của APK chuẩn. Đây là gói chưa ký bằng upload key của chủ tài khoản. Mẫu Part 3 thực chỉ được cấp cho source set assets của `localPreview` từ thư mục .tooling cục bộ.

## Thay đổi kỹ thuật

| Tệp | Thay đổi |
|---|---|
| `android-app/app/build.gradle.kts` và `app/src/localPreview/AndroidManifest.xml` | Package và nhãn Lab riêng. Build Debug/Release mặc định giữ nội dung synthetic. |
| `app/src/main/java/vn/toeiclearning/alpha/ui/LocalListeningPlayer.kt`, `domain/ListeningDemo.kt` | Dùng cùng MediaPlayer cho WAV và MP3. Chuyển đọc và xác thực SHA-256 sang luồng I/O. Hủy kết quả kiểm tra đang chờ nếu người dùng dừng, Back hoặc đưa app xuống nền. |
| `ui/ListeningDemoScreen.kt`, `ui/LocalPart3Demo.kt` | Kiểm tra lại thứ tự câu và liên kết audio trước khi hiển thị nhóm. Cuộn qua đúng ba câu và ghi lựa chọn tạm bằng Compose. |
| `android-app/scripts/prepare_local_part3_preview.py`, `tests/ingestion/test_local_part3_preview.py` | Tái dùng validator trên cả bốn nhóm, xuất riêng dữ liệu cần cho Part 3 vào .tooling và loại mọi trường đáp án. Bốn test mới dùng fixture tự tạo. |

Tham chiếu kỹ thuật FR-003/AT-03 (audio), FR-004/AT-04 (Reading), FR-009/AT-09 (chọn), FR-011/AT-11 (Full Mock) và Design V0.3. Stage05 vẫn CONDITIONAL cho Development. G05-CP01..08 và CP trước ACTIVE, POL01..16 OPEN, B1/Full Mock khóa và ngân sách DEFERRED. QA/ECP chính thức `NOT RUN`.

## Đối chiếu dữ liệu nguồn

Đã chạy lại Android `MediaExtractor` và `c2.android.mp3.decoder` trên cả bốn nhóm cục bộ. Probe kiểm tra lại checksum, giải mã đủ tới EOS, PCM khác 0, 44,1 kHz stereo, thời lượng khớp manifest trong 150 ms. Android BitmapFactory đọc ảnh Part 1 581 × 358.

| Part / ID | Thứ tự câu | PCM | Đường dùng trong P0 |
|---|---|---:|---|
| 1 / `zenlish:40911` | Q1 | 23,197 s | PARTIAL, chỉ có nhãn lựa chọn. Kiểm tra MP3 và ảnh cục bộ. |
| 2 / `zenlish:40943` | Q7 | 21,159 s | PARTIAL, chỉ có nhãn lựa chọn. Kiểm tra MP3 cục bộ. |
| 3 / `zenlish:41021` | Q32–34 | 74,919 s | FETCHED. MP3 1.265.710 byte, SHA-256 `cf77cbe460cfe87cf4a396fcb9b90194773c7bfeeb97f98e333e494fb2dcae4b`. Gói lab ghép clip này với ba câu đúng thứ tự. |
| 4 / `zenlish:41104` | Q71–73 | 77,401 s | FETCHED. Kiểm tra kỹ thuật cục bộ. |

Manifest cho bốn nhóm trả `HOLD` do còn thiếu kiểm chứng học liệu và đáp án. Trạng thái dữ liệu nguồn giữ nguyên. Đối chiếu ngữ nghĩa lời nghe với câu hỏi/ảnh và xác minh khóa của cả tám câu `NOT RUN`. [Hash và metadata nguồn](STAGE05_FASTTRACK_48H_ENGINEERING_REPORT_V0.1.md#đối-chiếu-zenlish-cục-bộ)

## Build và gói cục bộ

| Kiểm chứng từ thư mục `android-app/` | Kết quả |
|---|---|
| `python -B -X utf8 scripts/prepare_local_part3_preview.py` | PASS, exit 0. Dùng manifest đã tải, không cần HTTP. Sau bước này, `gradlew.bat :app:assembleLocalPreview` tạo APK lab. |
| `gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest :app:testReleaseUnitTest :app:bundleRelease` | PASS, exit 0. Release lint vital đã thực thi. |
| XML JUnit Debug / LocalPreview / Release | PASS 12/12 cho từng biến thể, không failure, error hoặc skip. |
| Ba scope guard Alpha / Beta Reading / CX-04 | PASS 10/11/9, exit 0. |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` và self-test parser | PASS 40/40, gồm 36 test trước và 4 test mới, exit 0. Self-test offline exit 0. |
| `scripts/run_pure_kotlin_core_checks.ps1` với JDK 17 và Kotlin CLI cục bộ | PASS 25 assertions, exit 0. |
| `scripts/listening_manifest.py .tooling/listening-overnight/normalized_manifest.json` | HOLD, exit 2. Bốn nhóm ánh xạ được, 0 lỗi cấu trúc, 24 hold. |
| `apksigner verify`, `bundletool validate`, kiểm tra manifest/ZIP | PASS, exit 0. APK và AAB chuẩn chỉ có bốn WAV synthetic. Đúng hai assets MP3 và JSON bổ sung có mặt trong APK lab. ZIP bàn giao chỉ gồm APK chuẩn, checksum, checklist và phiếu lỗi. |

Gói và các tệp checksum nằm trong `android-app/.tooling/fasttrack-handoff/`.

| Tệp | SHA-256 |
|---|---|
| `TOEIC-FastTrack-P0-2-may-0.2.1.zip` | `ce77e2019d691837b077929091b88e8937469aef342b4808fdbafc5af8f0d345` |
| `TOEIC-P0-0.2.1.apk` | `f8c499e1c3903398d09e68cb9a4f193c0a27df76d48f0572ebcb42aa812c970d` |
| `TOEIC-Part3-0.2.1-LAB.apk` | `f254003bbbab243407e686d39f78ba483f2bf9121dd2f8a21fe1bc9a9821fddb` |
| `TOEIC-0.2.1-PLAY-unsigned.aab` | `c7a23e5b05f3eb51304ec40a3c960a15787c42e56f5790958451d3c2d82deda3` |

## Kiểm thử và quyết định

Android Emulator API 34 ở 360dp, Wi-Fi và dữ liệu di động tắt. Bản Lab dùng chung layout và trình phát với APK chuẩn. Lần đầu bộ điều khiển thử nghiệm gọi nhầm tên Activity khi package có hậu tố và trả exit 1. Đã dùng tên lớp đầy đủ từ manifest và chạy lại cùng APK.

| Trường hợp | Kết quả |
|---|---|
| Lab phát Q32–34, chọn A trên từng câu để kiểm tra UI, tạm dừng, tiếp tục, đưa app xuống nền, phát đến hết, phát lại và Back | PASS, exit 0. Thu PCM từ loa ảo qua gRPC localhost, có 92 cửa sổ 100 ms có tín hiệu trên ngưỡng kiểm tra. Bản thu idle không có tín hiệu trên ngưỡng. |
| Lab thiếu MP3 | PASS, exit 0. Hai lượt phát đều báo thiếu audio và Back được. |
| Lab MP3 sai checksum | PASS, exit 0. Hai lượt phát đều báo tệp không khớp và Back được. |
| Lab dữ liệu giải mã lỗi sau khi kiểm checksum | PASS, exit 0. Cố tình tạo tệp không giải mã được và cập nhật hash tương ứng cho bản test. App báo không thể phát, cho thử lại và Back. |
| Lab đảo danh sách câu gắn với audio | PASS, exit 0. App từ chối nhóm và không hiện nút phát. |
| APK chuẩn phát tone, tạm dừng, đưa xuống nền, phát hết, phát lại và Back | PASS, exit 0 cho kịch bản APK chuẩn. Picker hiện Part 3 synthetic. |
| APK chuẩn Reading Part 5, giải thích mẫu, thay câu và quay lại, giữ lựa chọn qua các màn hình, xóa, khóa Full Mock | PASS trong cùng kịch bản. Bộ đếm về 0 sau xác nhận xóa. |
| Máy A và Máy B | NOT RUN. ADB không thấy điện thoại Android thật trong phiên này. Checklist và phiếu ghi lỗi đã có trong ZIP. |

**GO cho gói bàn giao kỹ thuật và DEMO Part 3 trong lab. NO-GO để xác nhận đợt thử hai người đã hoàn tất.** Issue #7 giữ mở để ghi kết quả trên hai máy có đồng thuận. Sáu baseline/guardrail vẫn khớp SHA-256. APK, AAB, ZIP, dữ liệu học liệu, bản thu và log thô giữ trong khu vực cục bộ. Bản sao XML JUnit nằm ở `android-app/.tooling/fasttrack-handoff/junit/`.

## Kiểm tra lại gói v0.2.1 trên nhánh mới nhất

Ngày 22/11/2026, đồng bộ nhánh với commit `aacf8445ce49c7539513af5483ec4a3498aeb758`. Gradle offline chạy lại `:app:assembleDebug`, `:app:assembleLocalPreview`, `:app:bundleRelease` và buộc chạy lại ba task JUnit bằng `--rerun`. Exit 0. Mỗi biến thể có 12 test PASS, không failure, error hoặc skip. Ba scope guard, 40 test ingestion, self-test parser và 25 assertions Kotlin đều PASS. Validator bốn nhóm trả `HOLD`, cùng 0 lỗi cấu trúc và 24 hold.

SHA-256 của cả hai APK trong thư mục bàn giao và AAB trùng với đầu ra Gradle. Chữ ký APK và `bundletool validate` trả exit 0. Đã kiểm tra lại CRC và bốn tệp trong ZIP, checksum APK trích từ ZIP, bốn WAV synthetic trong APK/AAB chuẩn và audio–Q32–34 trong APK Lab. Sáu baseline/guardrail tiếp tục khớp checksum. Bằng chứng của lượt này lưu cục bộ trong `android-app/.tooling/fasttrack-handoff/head-recheck/`.

Emulator API 34 giải mã lại cả bốn MP3 và ảnh Part 1, exit 0. Hộp thoại ANR của `com.android.systemui` che ứng dụng sau cold boot, làm bốn kịch bản UI trả exit 1 ở bước mở Listening. Xác nhận qua window dump, chọn **Wait**, rồi chạy lại trên cùng APK. Bản synthetic qua các ca phát, tạm dừng, chạy nền, phát lại, chọn và xem lại Reading, xóa lựa chọn và kiểm tra khóa Full Mock. Lab qua ca phát, dừng, phát lại và Back trong lượt này. Bốn ca thiếu MP3, sai checksum, dữ liệu decoder từ chối và sai thứ tự liên kết đều có exit 0 sau kiểm tra lại.

**GO cho gói bàn giao v0.2.1.** Lượt này không tái hiện lỗi P0/P1 trong các kịch bản đã thử. Mã ứng dụng và tệp bàn giao giữ nguyên. Smoke test hai máy vẫn **NOT RUN (0/2)** vì ADB chỉ nhận emulator trong lượt kiểm tra. Issue #7 tiếp tục mở.

## Play Internal Testing — thông tin từ chủ tài khoản

1. **Package ID**. Xác nhận `vn.toeiclearning.alpha` là package muốn đăng ký và versionCode 3 chưa được dùng trên Console. [Thiết lập app Play Console](https://support.google.com/googleplay/android-developer/answer/9859152)
2. **Upload key**. Xác nhận alias và fingerprint SHA-256 của chứng thư upload. Chủ tài khoản giữ key và ký AAB trong quy trình của họ. [Play App Signing](https://developer.android.com/studio/publish/app-signing)
3. **Hỗ trợ người dùng**. Cung cấp email hỗ trợ có người theo dõi và tên đơn vị hoặc nhà phát triển hiển thị. [Thiết lập app Play Console](https://support.google.com/googleplay/android-developer/answer/9859152)
4. **Privacy URL**. Cung cấp URL công khai của chính sách cho bản synthetic và đầu mối quyền riêng tư. [Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311)
5. **Loại tài khoản**. Xác nhận Personal hay Organization, tình trạng xác minh, ngày tạo nếu Personal và người có quyền quản lý Internal Testing. [Internal testing](https://support.google.com/googleplay/android-developer/answer/9845334)

Trạng thái upload Play `NOT RUN`. Các xác nhận này cần do chủ tài khoản thực hiện trước khi triển khai trên Console.
