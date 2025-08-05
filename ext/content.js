function sendPresenceData() {
    const video = document.querySelector("video");
    if (!video) {
        console.log("❌ Видео не найдено");
        return;
    }

    const title = document.title;
    const currentTime = video.currentTime;
    const duration = video.duration;

    console.log("📤 Отправка данных:", title, currentTime, duration);

    fetch("http://127.0.0.1:3333/anime", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title,
            currentTime,
            duration
        })
    }).then(res => {
        console.log("✅ Успешно отправлено");
    }).catch(err => {
        console.error("🚫 Ошибка отправки:", err);
    });
}

window.addEventListener('beforeunload', () => {
  const url = 'http://localhost:2222/api/activity_end';
  const data = 'type=anime'; // urlencoded строка
  const blob = new Blob([data], { type: 'application/x-www-form-urlencoded' });
  navigator.sendBeacon(url, blob);
});


setInterval(sendPresenceData, 7000);