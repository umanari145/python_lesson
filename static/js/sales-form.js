/**
 * 売上フォーム用JavaScript
 * 商品選択時に価格情報を表示する
 */

class SalesFormHandler {
    constructor(productPrices, fieldId) {
        this.productPrices = productPrices;
        this.productSelect = document.getElementById(fieldId);
        this.priceInfo = document.getElementById('product-price-info');
        this.priceDisplay = document.getElementById('product-price');
        
        this.init();
    }
    
    /**
     * 初期化
     */
    init() {
        if (!this.productSelect) {
            console.error('商品選択フィールドが見つかりません');
            return;
        }
        
        // 商品選択イベントリスナーを設定
        this.productSelect.addEventListener('change', () => this.handleProductChange());
        
        // 初期表示時に商品が選択されている場合は価格を表示
        if (this.productSelect.value) {
            this.handleProductChange();
        }
    }
    
    /**
     * 商品選択変更時の処理
     */
    handleProductChange() {
        const selectedProductId = this.productSelect.value;
        
        if (selectedProductId && this.productPrices[selectedProductId]) {
            this.displayPrice(this.productPrices[selectedProductId]);
        } else {
            this.hidePrice();
        }
    }
    
    /**
     * 価格を表示
     * @param {string} price - 価格
     */
    displayPrice(price) {
        const priceValue = parseFloat(price);
        const formattedPrice = priceValue.toLocaleString('ja-JP');
        
        this.priceDisplay.textContent = formattedPrice;
        this.priceInfo.classList.remove('hidden');
    }
    
    /**
     * 価格表示を非表示
     */
    hidePrice() {
        this.priceInfo.classList.add('hidden');
    }
}

/**
 * DOMContentLoaded時に初期化
 */
document.addEventListener('DOMContentLoaded', () => {
    // グローバル変数から商品価格情報とフィールドIDを取得
    if (typeof window.salesFormConfig !== 'undefined') {
        const { productPrices, fieldId } = window.salesFormConfig;
        new SalesFormHandler(productPrices, fieldId);
    } else {
        console.error('salesFormConfigが定義されていません');
    }
});

