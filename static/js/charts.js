document.addEventListener('DOMContentLoaded', () => {
    const dataEl = document.getElementById('chart-data');
    if (!dataEl) return;

    const {
        totalIncome = 0,
        totalExpense = 0,
        expenseLabels = [],
        expenseValues = [],
        coverageClamped = 0
    } = JSON.parse(dataEl.textContent);

    // 커버율 진행바 설정
    const coverageBar = document.getElementById('coverageProgress');
    if (coverageBar) {
        const pct = Number(coverageClamped) || 0;
        coverageBar.style.width = `${pct}%`;
    }

    const colors = {
        income: '#0ea5e9',
        expense: '#ef4444',
        expensePalette: ['#0ea5e9', '#f59e0b', '#10b981', '#6366f1', '#ef4444', '#a855f7']
    };

    const incomeExpenseEl = document.getElementById('incomeExpenseChart');
    if (incomeExpenseEl && window.Chart) {
        new Chart(incomeExpenseEl.getContext('2d'), {
            type: 'bar',
            data: {
                labels: ['수입', '지출'],
                datasets: [{
                    label: '금액',
                    data: [totalIncome, totalExpense],
                    backgroundColor: [colors.income, colors.expense],
                    borderRadius: 10,
                    barThickness: 48
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => new Intl.NumberFormat().format(ctx.parsed.y) + ' 원'
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: (value) => new Intl.NumberFormat().format(value) + '원'
                        }
                    }
                }
            }
        });
    }

    const expensePieEl = document.getElementById('expensePieChart');
    if (expensePieEl && window.Chart) {
        new Chart(expensePieEl.getContext('2d'), {
            type: 'doughnut',
            data: {
                labels: expenseLabels,
                datasets: [{
                    data: expenseValues,
                    backgroundColor: colors.expensePalette
                }]
            },
            options: {
                responsive: true,
                cutout: '60%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { boxWidth: 12 }
                    },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => `${ctx.label}: ${new Intl.NumberFormat().format(ctx.parsed)} 원`
                        }
                    }
                }
            }
        });
    }
});
