# Stage05 V6.7 — External primary-source evidence used for preliminary handoff guidance

**Purpose:** Current platform context; sources do not validate app code, product QA or any ARCH03 option. Pages accessed in planning on 2026-11-21.

| Source | Grounded relevance | Does NOT prove |
|---|---|---|
| [Android app architecture recommendations](https://developer.android.com/topic/architecture/recommendations) | Android strongly recommends Compose for new UIs, separation of concerns and unidirectional data flow | Our implementation works or is tested |
| [Android Compose-first](https://developer.android.com/develop/ui/compose/first) | Current first-party Compose UI direction | UI V0.3 satisfies accessibility without real Android checking |
| [UI layer / unidirectional flow](https://developer.android.com/topic/architecture/ui-layer) | States and events belong in separate roles/layers | Durable ACK or data trust |
| [Android Room](https://developer.android.com/training/data-storage/room) | Structured local persistence option on Android | Remote acknowledged answer, cross-reboot clock authority |
| [Android Media3](https://developer.android.com/media/media3) | Android audio player/media APIs | Listening uninterrupted on every device |
| [Flutter platform channels](https://docs.flutter.dev/platform-integration/platform-channels) | Flutter can invoke Android native APIs, at integration cost | Flutter is invalid or slower |

**Policy:** Do not hardcode claimed 'latest' versions from a snapshot; Codex must check current official stable versions at implementation time. Do not include other apps' copyrighted source code, assets or real TOEIC material in generated project.
