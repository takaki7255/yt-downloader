from yt_dlp import YoutubeDL

# ユーザーにYouTubeビデオのURLを入力するよう求める
video_url = input("ダウンロードするYouTubeビデオのURLを入力してください\n")

# ydl_optsでダウンロードオプションを設定
ydl_opts = {
    "outtmpl": "downloads/%(title)s.%(ext)s",  # ダウンロード先のディレクトリとファイル名
}

# ダウンローダーの作成
with YoutubeDL(ydl_opts) as ydl:
    # ダウンロード
    ydl.download([video_url])
