/**
 * Game Design Blog — main.js v2
 * 导航菜单、滚动动画、阅读时间
 */

document.addEventListener('DOMContentLoaded', () => {

  // ============ Mobile menu toggle ============
  const menuToggle = document.getElementById('menuToggle');
  const mainNav = document.getElementById('mainNav');

  if (menuToggle && mainNav) {
    menuToggle.addEventListener('click', () => {
      mainNav.classList.toggle('open');
    });

    mainNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('open');
      });
    });
  }

  // ============ Active nav highlighting ============
  const currentPath = window.location.pathname;
  document.querySelectorAll('.main-nav a').forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');
    if (href === currentPath.split('/').pop()) {
      link.classList.add('active');
    }
    if (currentPath.includes('/posts/') && href && href.includes('blog.html')) {
      link.classList.add('active');
    }
  });

  // ============ Reading time estimate ============
  const postContent = document.querySelector('.post-content');
  if (postContent) {
    const text = postContent.textContent || '';
    const chineseChars = (text.match(/[一-鿿　-〿＀-￯]/g) || []).length;
    const enWords = (text.match(/[a-zA-Z]+/g) || []).length;
    const totalWords = chineseChars + enWords;
    const readingTime = Math.max(1, Math.ceil(totalWords / 300));

    const meta = document.querySelector('.post-header .post-meta');
    if (meta) {
      const timeBadge = document.createElement('span');
      timeBadge.className = 'reading-time';
      timeBadge.textContent = `· ☕ ${readingTime} 分钟`;
      meta.appendChild(timeBadge);
    }
  }

  // ============ Scroll reveal animation ============
  const revealElements = document.querySelectorAll('.fade-in');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animationPlayState = 'running';
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
  );

  revealElements.forEach(el => {
    el.style.animationPlayState = 'paused';
    observer.observe(el);
  });

  // ============ Navbar transparency on scroll ============
  const header = document.querySelector('.site-header');
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 80) {
      header.style.borderColor = 'rgba(30, 45, 68, 0.8)';
      header.style.background = 'rgba(11, 20, 34, 0.92)';
    } else {
      header.style.borderColor = 'var(--border-dark)';
      header.style.background = 'rgba(11, 20, 34, 0.85)';
    }
    lastScroll = currentScroll;
  });

  console.log(`🎮 Game Design Blog · ${new Date().toLocaleDateString('zh-CN')}`);
});
