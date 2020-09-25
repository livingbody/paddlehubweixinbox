import paddlehub as hub
import cv2


def poem():
    readingPicturesWritingPoems = hub.Module(name="reading_pictures_writing_poems")
    results = readingPicturesWritingPoems.WritingPoem(
        images=[cv2.imread("scenery.jpg")],
        use_gpu=False)
    print(results)
    print(50 * '*')
    print(results[0]['Poetrys'])


if __name__ == '__main__':
    poem()
