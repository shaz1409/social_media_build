from src.opus_automation import automate_opus_clips
from src.social_media_posting import post_to_twitter

def main():
    # Call your automation functions here
    print("Starting the automation...")
    automate_opus_clips()
    post_to_twitter("path/to/your/video.mp4", "Check out my new video!")

if __name__ == "__main__":
    main()
