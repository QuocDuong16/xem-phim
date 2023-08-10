document.addEventListener("DOMContentLoaded", function () {
    const player = new Plyr('#player', {
        captions: {
            active: true,
            language: 'vi',
            update: true
        }
    });

    const changeVideoBtn = document.getElementById('changeVideoBtn');
    const videoName = document.getElementById('videoName');
    const videoInput = document.getElementById('videoInput');
    const changeSubtitleBtn = document.getElementById('changeSubtitleBtn');

    changeVideoBtn.addEventListener('click', function () {
        const newVideoSrc = videoInput.value;
        videoName.innerHTML = newVideoSrc;
        player.source = {
            type: 'video',
            sources: [
                {
                    src: newVideoSrc,
                    type: 'video/mp4',
                },
            ],
        };
    });

    changeSubtitleBtn.addEventListener('click', function () {
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = '.vtt'; // Chỉ chấp nhận file vtt
        fileInput.onchange = function (event) {
            const file = event.target.files[0];
            if (file) {
                const video = player.elements.container.querySelector('video');

                // Xóa các track phụ đề cũ
                const existingTracks = video.querySelectorAll('track[kind="captions"]');
                existingTracks.forEach(existingTrack => existingTrack.remove());

                const track = document.createElement('track');
                track.kind = 'captions';
                track.label = 'Subtitle';
                track.src = URL.createObjectURL(file); // Tạo URL từ file
                track.srclang = 'vi';
                track.default = true;

                video.appendChild(track);
            }
        };
        fileInput.click(); // Mở hộp thoại tải lên tập tin
    });
});