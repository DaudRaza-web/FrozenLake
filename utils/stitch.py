import cv2
import os

def images_to_video(image_prefix, num_images, output_video, fps=40):
    """
    Creates a video from a sequence of images.

    Parameters:
        image_prefix (str): Prefix of the image filenames.
        num_images (int): Number of images to stitch into the video.
        output_video (str): Filename of the output video.
        fps (int): Frames per second for the output video. Default is 10.

    Returns:
        None
    """
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (640, 480))  # Assuming images are 800x600

    # Stitch images into video
    for i in range(1, num_images + 1):
        image_file = f"{image_prefix}_{i}.png"
        if os.path.exists(image_file):
            image = cv2.imread(image_file)
            video_writer.write(image)
        else:
            print(f"File '{image_file}' not found.")
    
    # Release the VideoWriter object
    video_writer.release()
    print(f"Video saved as '{output_video}'.")

# Example usage:
images_to_video("nested_list_lengths_stacked", 200, "normal_dist.mp4")
