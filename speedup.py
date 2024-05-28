from moviepy.editor import VideoFileClip, vfx

def speed_up_video(input_path, output_path, speed_factor=1440):
    # Load the video file
    video = VideoFileClip(input_path)
    
    # Speed up the video
    sped_up_video = video.fx(vfx.speedx, speed_factor)
    
    # Write the result to a new file
    sped_up_video.write_videofile(output_path, codec="libx264")

if __name__ == "__main__":
    input_video_path = "input_video.mov"  # Replace with your input video file path
    output_video_path = "sped_up_video.mov"  # Replace with your desired output file path
    
    speed_up_video(input_video_path, output_video_path)
