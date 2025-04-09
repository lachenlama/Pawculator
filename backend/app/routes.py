from flask import Blueprint, request, jsonify, render_template
from .logic import NFTCalculator

routes = Blueprint('calculator', __name__)
calculator = NFTCalculator()

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/api/calculate', methods=['GET'])
def get_calculations():
    return jsonify(calculator.calculate_all())

@routes.route('/api/update', methods=['POST'])
def update_parameters():
    data = request.get_json()
    
    if 'nfts_staked' in data:
        calculator.staked_percent = float(data['nfts_staked']) / calculator.total_nfts
    
    if 'avg_bribe' in data:
        calculator.avg_bribe = float(data['avg_bribe'])
    
    if 'bera_price' in data:
        calculator.bera_price = float(data['bera_price'])
    
    if 'staked_percent' in data:
        calculator.staked_percent = float(data['staked_percent'])
    
    if 'user_nft_stake' in data:
        calculator.user_nft_stake = float(data['user_nft_stake'])

    return jsonify({'status': 'success', 'updated': data})
