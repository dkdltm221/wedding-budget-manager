document.addEventListener('DOMContentLoaded', function () {
    const editModalEl = document.getElementById('editModal');
    const editModal = editModalEl ? new bootstrap.Modal(editModalEl) : null;
    const searchModalEl = document.getElementById('searchModal');
    const searchModal = searchModalEl ? new bootstrap.Modal(searchModalEl) : null;

    const editForm = document.getElementById('editForm');
    const deleteForm = document.getElementById('deleteForm');

    function openEditModal(data) {
        if (!editModal || !editForm || !deleteForm) return;
        editForm.action = data.editUrl;
        deleteForm.action = data.deleteUrl;

        document.getElementById('editName').value = data.name || '';
        document.getElementById('editSide').value = data.side || 'groom';
        document.getElementById('editAmount').value = data.amount || 0;
        document.getElementById('editNote').value = data.note || '';

        if (searchModal) searchModal.hide();
        editModal.show();
    }

    document.querySelectorAll('[data-edit]').forEach(function (btn) {
        btn.addEventListener('click', function () {
            openEditModal({
                id: btn.dataset.id,
                name: btn.dataset.name,
                side: btn.dataset.side,
                amount: btn.dataset.amount,
                note: btn.dataset.note,
                editUrl: btn.dataset.editUrl,
                deleteUrl: btn.dataset.deleteUrl
            });
        });
    });

    document.querySelectorAll('[data-edit-from-search]').forEach(function (btn) {
        btn.addEventListener('click', function () {
            openEditModal({
                id: btn.dataset.id,
                name: btn.dataset.name,
                side: btn.dataset.side,
                amount: btn.dataset.amount,
                note: btn.dataset.note,
                editUrl: btn.dataset.editUrl,
                deleteUrl: btn.dataset.deleteUrl
            });
        });
    });

    const deleteButton = document.getElementById('deleteButton');
    if (deleteButton && deleteForm) {
        deleteButton.addEventListener('click', function () {
            if (confirm('정말 삭제할까요?')) {
                deleteForm.submit();
            }
        });
    }

    if (searchModalEl && searchModalEl.dataset.autoshow === 'true') {
        searchModal.show();
    }

    // 비율 진행바 설정
    const ratioEl = document.getElementById('guestRatioProgress');
    if (ratioEl) {
        const groomPct = Number(ratioEl.dataset.groom || 0);
        const bridePct = Number(ratioEl.dataset.bride || 0);
        const bars = ratioEl.querySelectorAll('.progress-bar');
        if (bars[0]) {
            bars[0].style.width = `${groomPct}%`;
            bars[0].setAttribute('aria-valuenow', groomPct);
        }
        if (bars[1]) {
            bars[1].style.width = `${bridePct}%`;
            bars[1].setAttribute('aria-valuenow', bridePct);
        }
    }
});
