<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trading Journal - Box Calendar</title>
    <style>
        :root {
            --bg: #ffffff;
            --card: #f7f6f3;
            --text: #37352f;
            --text-light: #787774;
            --green: #4caf50;
            --red: #f44336;
            --yellow: #ff9800;
            --blue: #2196f3;
            --border: #e9e9e7;
            --hover: #f1f1ef;
            --empty: #f0f0f0;
        }

        [data-theme="dark"] {
            --bg: #2f3437;
            --card: #3d4245;
            --text: #ffffff;
            --text-light: #b5b5b5;
            --border: #5a5a5a;
            --hover: #4a4f52;
            --empty: #4a4f52;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border);
        }

        .stats-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: var(--card);
            padding: 20px;
            border-radius: 8px;
            border: 1px solid var(--border);
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .stat-win { color: var(--green); }
        .stat-loss { color: var(--red); }
        .stat-total { color: var(--blue); }

        .calendar {
            background: var(--card);
            border-radius: 8px;
            border: 1px solid var(--border);
            padding: 20px;
            margin-bottom: 30px;
        }

        .calendar-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 4px;
        }

        .calendar-day-header {
            text-align: center;
            font-weight: 600;
            color: var(--text-light);
            padding: 8px;
            font-size: 0.9rem;
        }

        .calendar-day {
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
            cursor: pointer;
            position: relative;
            border: 2px solid transparent;
            transition: all 0.2s;
            font-weight: 500;
        }

        .calendar-day.empty {
            background: var(--empty);
            color: var(--text-light);
        }

        .calendar-day.has-trades {
            color: white;
            font-weight: 600;
        }

        .calendar-day.win-day {
            background: var(--green);
        }

        .calendar-day.loss-day {
            background: var(--red);
        }

        .calendar-day.mixed-day {
            background: var(--yellow);
        }

        .calendar-day:hover {
            transform: scale(1.05);
            border-color: var(--text);
        }

        .legend {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9rem;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }

        .legend-win { background: var(--green); }
        .legend-loss { background: var(--red); }
        .legend-mixed { background: var(--yellow); }
        .legend-empty { background: var(--empty); }

        .trades-list {
            background: var(--card);
            border-radius: 8px;
            border: 1px solid var(--border);
            padding: 20px;
        }

        .trade-item {
            display: grid;
            grid-template-columns: 100px 80px 100px 1fr 100px 100px 100px 60px;
            gap: 12px;
            padding: 12px;
            border-bottom: 1px solid var(--border);
            align-items: center;
        }

        .trade-item:hover {
            background: var(--hover);
        }

        .trade-header {
            font-weight: 600;
            color: var(--text-light);
            border-bottom: 2px solid var(--border);
        }

        .win { color: var(--green); }
        .loss { color: var(--red); }

        .pill {
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .pill.win { background: rgba(76, 175, 80, 0.1); }
        .pill.loss { background: rgba(244, 67, 54, 0.1); }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1000;
        }

        .modal-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: var(--card);
            padding: 30px;
            border-radius: 8px;
            max-width: 500px;
            width: 90%;
            max-height: 80vh;
            overflow-y: auto;
        }

        .btn {
            padding: 8px 16px;
            border: 1px solid var(--border);
            background: var(--card);
            color: var(--text);
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn:hover {
            background: var(--hover);
        }

        .theme-toggle {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--text);
        }

        @media (max-width: 768px) {
            .trade-item {
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }
            
            .trade-header {
                display: none;
            }
            
            .calendar-day {
                font-size: 0.8rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Trading Journal</h1>
            <button class="theme-toggle" onclick="toggleTheme()">🌓</button>
        </div>

        <div class="stats-cards">
            <div class="stat-card">
                <div class="stat-number stat-total" id="totalTrades">0</div>
                <div>Total Trades</div>
            </div>
            <div class="stat-card">
                <div class="stat-number stat-win" id="winRate">0%</div>
                <div>Win Rate</div>
            </div>
            <div class="stat-card">
                <div class="stat-number stat-win" id="totalWins">0</div>
                <div>Winning Trades</div>
            </div>
            <div class="stat-card">
                <div class="stat-number stat-loss" id="totalLosses">0</div>
                <div>Losing Trades</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="netPnl">$0</div>
                <div>Net P&L</div>
            </div>
        </div>

        <div class="calendar">
            <div class="calendar-header">
                <h3 id="currentMonth">January 2024</h3>
                <div>
                    <button class="btn" onclick="changeMonth(-1)">← Prev</button>
                    <button class="btn" onclick="changeMonth(1)">Next →</button>
                </div>
            </div>
            <div class="calendar-grid" id="calendarDays">
                <!-- Calendar will be generated here -->
            </div>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color legend-win"></div>
                    <span>All Wins</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color legend-loss"></div>
                    <span>All Losses</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color legend-mixed"></div>
                    <span>Mixed Results</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color legend-empty"></div>
                    <span>No Trades</span>
                </div>
            </div>
        </div>

        <div class="trades-list">
            <div class="trade-item trade-header">
                <div>Date</div>
                <div>Pair</div>
                <div>Direction</div>
                <div>Strategy</div>
                <div>Entry</div>
                <div>Exit</div>
                <div>P&L</div>
                <div>Result</div>
            </div>
            <div id="tradesContainer">
                <!-- Trades will be listed here -->
            </div>
        </div>
    </div>

    <div class="modal" id="dayModal">
        <div class="modal-content">
            <h3 id="modalDate">Date Details</h3>
            <div id="modalTrades">
                <!-- Day trades will be shown here -->
            </div>
            <button class="btn" onclick="closeModal()" style="margin-top: 20px;">Close</button>
        </div>
    </div>

    <script>
        // Sample trading data
        let trades = [
            {
                id: 1,
                date: '2024-01-15',
                pair: 'EUR/USD',
                direction: 'Long',
                strategy: 'Breakout',
                entry: 1.0950,
                exit: 1.0985,
                pnl: 35,
                result: 'win',
                notes: 'Clean breakout above resistance'
            },
            {
                id: 2,
                date: '2024-01-15',
                pair: 'GBP/USD',
                direction: 'Short',
                strategy: 'Pullback',
                entry: 1.2750,
                exit: 1.2720,
                pnl: 30,
                result: 'win',
                notes: 'Short on retest of broken support'
            },
            {
                id: 3,
                date: '2024-01-14',
                pair: 'USD/JPY',
                direction: 'Long',
                strategy: 'Trend',
                entry: 145.20,
                exit: 144.80,
                pnl: -40,
                result: 'loss',
                notes: 'Failed breakout, stopped out'
            },
            {
                id: 4,
                date: '2024-01-13',
                pair: 'EUR/USD',
                direction: 'Short',
                strategy: 'Reversal',
                entry: 1.0980,
                exit: 1.0960,
                pnl: 20,
                result: 'win',
                notes: 'Nice reversal at resistance'
            },
            {
                id: 5,
                date: '2024-01-12',
                pair: 'AUD/USD',
                direction: 'Long',
                strategy: 'Breakout',
                entry: 0.6720,
                exit: 0.6700,
                pnl: -20,
                result: 'loss',
                notes: 'False breakout'
            },
            {
                id: 6,
                date: '2024-01-11',
                pair: 'EUR/USD',
                direction: 'Long',
                strategy: 'Trend',
                entry: 1.0920,
                exit: 1.0950,
                pnl: 30,
                result: 'win',
                notes: 'Trend continuation'
            },
            {
                id: 7,
                date: '2024-01-11',
                pair: 'GBP/USD',
                direction: 'Short',
                strategy: 'Reversal',
                entry: 1.2780,
                exit: 1.2800,
                pnl: -20,
                result: 'loss',
                notes: 'Early reversal call'
            },
            {
                id: 8,
                date: '2024-01-10',
                pair: 'USD/CAD',
                direction: 'Long',
                strategy: 'Breakout',
                entry: 1.3400,
                exit: 1.3370,
                pnl: -30,
                result: 'loss',
                notes: 'False breakout'
            },
            {
                id: 9,
                date: '2024-01-09',
                pair: 'EUR/USD',
                direction: 'Short',
                strategy: 'Pullback',
                entry: 1.0970,
                exit: 1.0940,
                pnl: 30,
                result: 'win',
                notes: 'Perfect pullback entry'
            },
            {
                id: 10,
                date: '2024-01-08',
                pair: 'GBP/USD',
                direction: 'Long',
                strategy: 'Trend',
                entry: 1.2720,
                exit: 1.2750,
                pnl: 30,
                result: 'win',
                notes: 'Strong trend day'
            }
        ];

        let currentDate = new Date();
        let currentMonth = currentDate.getMonth();
        let currentYear = currentDate.getFullYear();

        // Initialize
        function init() {
            updateStats();
            renderCalendar();
            renderTrades();
        }

        // Update statistics
        function updateStats() {
            const totalTrades = trades.length;
            const wins = trades.filter(t => t.result === 'win').length;
            const losses = trades.filter(t => t.result === 'loss').length;
            const winRate = totalTrades > 0 ? ((wins / totalTrades) * 100).toFixed(1) : 0;
            const netPnl = trades.reduce((sum, trade) => sum + trade.pnl, 0);

            document.getElementById('totalTrades').textContent = totalTrades;
            document.getElementById('winRate').textContent = winRate + '%';
            document.getElementById('totalWins').textContent = wins;
            document.getElementById('totalLosses').textContent = losses;
            document.getElementById('netPnl').textContent = '$' + netPnl;
        }

        // Render calendar with colored boxes
        function renderCalendar() {
            const calendarDays = document.getElementById('calendarDays');
            const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
                               'July', 'August', 'September', 'October', 'November', 'December'];
            
            document.getElementById('currentMonth').textContent = 
                `${monthNames[currentMonth]} ${currentYear}`;

            // Clear calendar
            calendarDays.innerHTML = '';

            // Add day headers
            const dayHeaders = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
            dayHeaders.forEach(day => {
                const dayEl = document.createElement('div');
                dayEl.className = 'calendar-day-header';
                dayEl.textContent = day;
                calendarDays.appendChild(dayEl);
            });

            // Get first day of month
            const firstDay = new Date(currentYear, currentMonth, 1).getDay();
            const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

            // Add empty days for padding
            for (let i = 0; i < firstDay; i++) {
                const emptyDay = document.createElement('div');
                emptyDay.className = 'calendar-day empty';
                calendarDays.appendChild(emptyDay);
            }

            // Add days of month
            for (let day = 1; day <= daysInMonth; day++) {
                const dayEl = document.createElement('div');
                dayEl.className = 'calendar-day';
                dayEl.textContent = day;

                const dateStr = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
                const dayTrades = trades.filter(t => t.date === dateStr);

                if (dayTrades.length > 0) {
                    dayEl.classList.add('has-trades');
                    const wins = dayTrades.filter(t => t.result === 'win').length;
                    const losses = dayTrades.filter(t => t.result === 'loss').length;
                    
                    if (wins > 0 && losses === 0) {
                        dayEl.classList.add('win-day');
                    } else if (losses > 0 && wins === 0) {
                        dayEl.classList.add('loss-day');
                    } else {
                        dayEl.classList.add('mixed-day');
                    }
                } else {
                    dayEl.classList.add('empty');
                }

                dayEl.onclick = () => showDayDetails(day);
                calendarDays.appendChild(dayEl);
            }
        }

        // Render trades list
        function renderTrades() {
            const container = document.getElementById('tradesContainer');
            container.innerHTML = '';

            trades.sort((a, b) => new Date(b.date) - new Date(a.date)).forEach(trade => {
                const tradeEl = document.createElement('div');
                tradeEl.className = 'trade-item';
                tradeEl.innerHTML = `
                    <div>${formatDate(trade.date)}</div>
                    <div>${trade.pair}</div>
                    <div>${trade.direction}</div>
                    <div>${trade.strategy}</div>
                    <div>${trade.entry}</div>
                    <div>${trade.exit}</div>
                    <div class="${trade.pnl >= 0 ? 'win' : 'loss'}">${trade.pnl >= 0 ? '+' : ''}${trade.pnl}</div>
                    <div class="pill ${trade.result}">${trade.result === 'win' ? 'WIN' : 'LOSS'}</div>
                `;
                container.appendChild(tradeEl);
            });
        }

        // Show day details in modal
        function showDayDetails(day) {
            const dateStr = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
            const dayTrades = trades.filter(t => t.date === dateStr);
            
            document.getElementById('modalDate').textContent = `Trades on ${formatDate(dateStr)}`;
            
            const modalTrades = document.getElementById('modalTrades');
            modalTrades.innerHTML = '';

            if (dayTrades.length === 0) {
                modalTrades.innerHTML = '<p>No trades on this day</p>';
            } else {
                dayTrades.forEach(trade => {
                    const tradeEl = document.createElement('div');
                    tradeEl.style.padding = '12px';
                    tradeEl.style.borderBottom = '1px solid var(--border)';
                    tradeEl.style.marginBottom = '12px';
                    tradeEl.innerHTML = `
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <strong>${trade.pair} ${trade.direction}</strong>
                            <span class="${trade.result === 'win' ? 'win' : 'loss'}">${trade.pnl >= 0 ? '+' : ''}${trade.pnl} pips</span>
                        </div>
                        <div style="color: var(--text-light); font-size: 0.9rem;">
                            <div>Strategy: ${trade.strategy}</div>
                            <div>Entry: ${trade.entry} | Exit: ${trade.exit}</div>
                            <div style="margin-top: 8px; font-style: italic;">${trade.notes}</div>
                        </div>
                    `;
                    modalTrades.appendChild(tradeEl);
                });
            }

            document.getElementById('dayModal').style.display = 'block';
        }

        // Utility functions
        function formatDate(dateStr) {
            const date = new Date(dateStr);
            return date.toLocaleDateString('en-US', { 
                month: 'short', 
                day: 'numeric',
                year: 'numeric'
            });
        }

        function closeModal() {
            document.getElementById('dayModal').style.display = 'none';
        }

        function changeMonth(direction) {
            currentMonth += direction;
            if (currentMonth < 0) {
                currentMonth = 11;
                currentYear--;
            } else if (currentMonth > 11) {
                currentMonth = 0;
                currentYear++;
            }
            renderCalendar();
        }

        function toggleTheme() {
            const isDark = document.body.hasAttribute('data-theme');
            if (isDark) {
                document.body.removeAttribute('data-theme');
            } else {
                document.body.setAttribute('data-theme', 'dark');
            }
        }

        // Initialize on load
        document.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>