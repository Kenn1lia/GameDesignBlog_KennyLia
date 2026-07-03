/**
 * Game Design Blog — main.js
 * 导航菜单、页面交互
 */

document.addEventListener('DOMContentLoaded', () => {

  // ============ Mobile menu toggle ============
  const menuToggle = document.getElementById('menuToggle');
  const mainNav = document.getElementById('mainNav');

  if (menuToggle && mainNav) {
    menuToggle.addEventListener('click', () => {
      mainNav.classList.toggle('open');
    });

    // 点击导航链接后关闭菜单
    mainNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('open');
      });
    });
  }

  // ============ 自动为文章页设置返回链接高亮 ============
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.main-nav a');
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === currentPath.split('/').pop()) {
      link.classList.add('active');
    }
    // 博文页面高亮"文章"导航
    if (currentPath.includes('/posts/') && link.getAttribute('href').includes('blog.html')) {
      link.classList.add('active');
    }
  });

  // ============ 文章阅读时间估算（为 post-content 区域） ============
  const postContent = document.querySelector('.post-content');
  if (postContent) {
    const text = postContent.textContent || '';
    // 中文阅读速度约 300 字/分钟
    const chineseChars = text.match(/[一-鿿　-〿＀-￯]/g);
    const wordCount = chineseChars ? chineseChars.length : 0;
    const enWords = text.match(/[a-zA-Z]+/g);
    const enCount = enWords ? enWords.length : 0;
    const totalWords = wordCount + enCount;
    const readingTime = Math.max(1, Math.ceil(totalWords / 300));

    const meta = document.querySelector('.post-header .post-meta');
    if (meta) {
      const timeBadge = document.createElement('span');
      timeBadge.textContent = `· ☕ ${readingTime} 分钟阅读`;
      timeBadge.style.color = 'var(--text-muted)';
      meta.appendChild(timeBadge);
    }
  }

  // ============ 页面淡入动画 ============
  const fadeElements = document.querySelectorAll('.fade-in');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationDelay = '0.1s';
        entry.target.style.animationPlayState = 'running';
      }
    });
  }, { threshold: 0.1 });

  fadeElements.forEach(el => {
    el.style.animationPlayState = 'paused';
    observer.observe(el);
  });

  console.log(`🎮 Game Design Blog loaded · ${new Date().toLocaleDateString('zh-CN')}`);
});
