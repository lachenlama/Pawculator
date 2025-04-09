document.addEventListener('DOMContentLoaded', function() {
    // Initialize form and elements
    const form = document.getElementById('calculator-form');
    const stakedPercent = document.getElementById('stakedPercent');
    const stakedPercentValue = document.getElementById('stakedPercentValue');
    
    // Update percentage display when slider changes
    stakedPercent.addEventListener('input', function() {
        stakedPercentValue.textContent = `${this.value}%`;
    });

    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        updateCalculations();
    });

    // Initial load
    updateCalculations();
});

async function updateCalculations() {
    // Get input values
    const userNftStake = document.getElementById('userNftStake').value;
    const nftsStaked = document.getElementById('nftsStaked').value;
    const avgBribe = document.getElementById('avgBribe').value;
    const beraPrice = document.getElementById('beraPrice').value;
    const stakedPercent = document.getElementById('stakedPercent').value;

    // Update parameters via API
    await fetch('api/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_nft_stake: Number(userNftStake),
            nfts_staked: Number(nftsStaked), 
            avg_bribe: Number(avgBribe),
            bera_price: Number(beraPrice),
            staked_percent: Number(stakedPercent)/100
        })
    });

    // Get updated calculations
    const response = await fetch('api/calculate');
    const data = await response.json();

    // Update results table
    const resultsTable = document.getElementById('results-table');
    resultsTable.innerHTML = `
        <tr><th>NFT Price</th><td>$${data.price_per_nft}</td></tr>
        <tr><th>Your Staked Value</th><td>$${data.effective_amount_staked}</td></tr>
        <tr><th>POL Earnings/NFT</th><td>$${data.pol_earnings_per_nft}</td></tr>
        <tr><th>APR</th><td>${data.apr}%</td></tr>
        <tr><th>Total Bribes</th><td>$${data.total_bribes.toLocaleString()}</td></tr>
    `;
}
