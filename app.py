from flask import Flask, render_template, request, flash, redirect, url_for
from pytube import YouTube
import os
import getpass

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['videoUrl']
    username = getpass.getuser()  # Fetching the username of the current user

    if 'youtube.com' in video_url or 'youtu.be' in video_url:
        try:
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()

            # Define the download path to the user's Downloads folder
            download_path = os.path.join('/Users', username, 'Downloads')
            audio_stream.download(download_path)

            flash(f"Audio was saved in {download_path}")
        except Exception as e:
            flash(f'An error occurred: {e}')
    else:
        flash('Enter a valid YouTube video link.')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
