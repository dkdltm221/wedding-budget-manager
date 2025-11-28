document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('form[data-confirm]').forEach((form) => {
        form.addEventListener('submit', (e) => {
            const msg = form.getAttribute('data-confirm') || '정말 삭제할까요?';
            if (!confirm(msg)) {
                e.preventDefault();
            }
        });
    });
});
