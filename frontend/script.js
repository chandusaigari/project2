const API_URL = 'http://localhost:5000';

async function calculate() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operator = document.getElementById('operator').value;
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');

    errorDiv.textContent = '';
    resultDiv.textContent = 'Calculating...';

    if (num1 === '' || num2 === '') {
        errorDiv.textContent = '⚠️ Please enter both numbers.';
        resultDiv.textContent = 'Result: —';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/calculate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                num1: parseFloat(num1),
                num2: parseFloat(num2),
                operator: operator
            })
        });

        const data = await response.json();

        if (response.ok) {
            resultDiv.textContent = `Result: ${data.result}`;
            loadHistory();
        } else {
            errorDiv.textContent = `❌ Error: ${data.error}`;
            resultDiv.textContent = 'Result: —';
        }
    } catch (err) {
        errorDiv.textContent = '❌ Could not connect to server.';
        resultDiv.textContent = 'Result: —';
    }
}

async function loadHistory() {
    const tbody = document.getElementById('historyBody');
    tbody.innerHTML = '<tr><td colspan="6">Loading...</td></tr>';

    try {
        const response = await fetch(`${API_URL}/history`);
        const data = await response.json();

        if (!data.length) {
            tbody.innerHTML = '<tr><td colspan="6">No history yet.</td></tr>';
            return;
        }

        tbody.innerHTML = data.map((row, index) => `
            <tr>
                <td>${index + 1}</td>
                <td>${row.operand1}</td>
                <td>${row.operator}</td>
                <td>${row.operand2}</td>
                <td><strong>${row.result}</strong></td>
                <td>${row.created_at}</td>
            </tr>
        `).join('');
    } catch (err) {
        tbody.innerHTML = '<tr><td colspan="6">❌ Failed to load history.</td></tr>';
    }
}

// Load history on page load
window.onload = loadHistory;