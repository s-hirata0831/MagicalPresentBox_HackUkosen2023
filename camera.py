import cv2

def capture(path):
    cap = cv2.VideoCapture(0)

    # カメラを起動
    cap.open(0)

    # 写真を撮る
    ret, frame = cap.read()

    # 写真を保存する
    cv2.imwrite(path, frame)

    # カメラを終了する
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # 保存するパスを指定
    path = "./presentImg/post.jpg"

    # 写真を撮って保存する
    capture(path)
