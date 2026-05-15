
import cv2
import os


def extract_frames(video_path, output_dir="data/frames", step_seconds=2):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Не удалось открыть видео: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_step = int(fps * step_seconds)

    saved_frames = []
    frame_id = 0
    saved_id = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_id % frame_step == 0:
            timestamp_ms = cap.get(cv2.CAP_PROP_POS_MSEC)

            frame_name = f"frame_{saved_id:04d}_{int(timestamp_ms)}ms.jpg"
            frame_path = os.path.join(output_dir, frame_name)

            cv2.imwrite(frame_path, frame)

            saved_frames.append({
                "frame_id": frame_id,
                "timestamp_ms": timestamp_ms,
                "frame_path": frame_path
            })

            saved_id += 1

        frame_id += 1

    cap.release()

    return saved_frames