const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const mode = process.argv[2] || 'preview';
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.resolve('index.html'));
  await page.waitForFunction(() => window.__ready === true);
  if (mode === 'preview') {
    const times = process.argv.slice(3).map(Number);
    for (const t of times) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: `frames/f_${String(t).replace('.', '_')}.png` });
    }
  } else {
    const fps = 30, dur = await page.evaluate(() => window.DURATION);
    const ff = spawn('ffmpeg', ['-y', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
      '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', 'out.mp4'], { stdio: ['pipe', 'ignore', 'inherit'] });
    for (let i = 0; i < dur * fps; i++) {
      await page.evaluate(t => window.render(t), i / fps);
      const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
  }
  await browser.close();
})();
