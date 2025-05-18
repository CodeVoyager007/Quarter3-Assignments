import streamlit as st
from typing import Dict, Any
from datetime import datetime, timedelta

# Simulated Stripe products
PRODUCTS = {
    "monthly": {
        "id": "price_monthly",
        "name": "Pro Monthly",
        "price": 9.99,
        "period": "month"
    },
    "yearly": {
        "id": "price_yearly",
        "name": "Pro Yearly",
        "price": 99.99,
        "period": "year"
    }
}
class Payment:
    def __init__(self):
        pass
    
    def get_products(self) -> Dict[str, Any]:
        """Get available subscription products."""
        return PRODUCTS
    
    def create_checkout_session(self, product_id: str) -> Dict[str, Any]:
        """Simulate creating a Stripe checkout session."""
        product = PRODUCTS.get(product_id)
        if not product:
            raise ValueError("Invalid product ID")
            
        # Simulate a successful payment
        return {
            "success": True,
            "session_id": f"dummy_session_{datetime.now().timestamp()}",
            "product": product
        }
    
    def process_payment(self, session_id: str) -> bool:
        """Simulate processing a successful payment."""
        return True
    
    def display_pricing(self) -> None:
        """Display pricing options with Streamlit."""
        st.markdown("## 🌟 Upgrade to Pro")
        st.markdown("### Unlock Premium Features")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### Monthly Plan
            - $9.99/month
            - HD Quality Posters
            - No Watermarks
            - Premium Fonts
            - Priority Support
            """)
            if st.button("Subscribe Monthly"):
                self._handle_subscription("monthly")
        
        with col2:
            st.markdown("""
            #### Yearly Plan
            - $99.99/year
            - All Monthly Features
            - 2 Months Free!
            - Custom Themes
            - API Access
            """)
            if st.button("Subscribe Yearly"):
                self._handle_subscription("yearly")
    
    def _handle_subscription(self, plan: str) -> None:
        """Handle subscription purchase."""
        try:
            session = self.create_checkout_session(plan)
            if session["success"]:
                st.success(f"""
                🎉 Thanks for subscribing to {session['product']['name']}!
                
                This is a demo, but in production:
                1. You would be redirected to Stripe
                2. Enter your payment details
                3. Get immediate access to Pro features
                """)
                
                # Store pro status in session
                st.session_state["subscription"] = "pro"
            else:
                st.error("Payment processing failed. Please try again.")
        except Exception as e:
            st.error(f"Error processing subscription: {str(e)}")

    def show_receipt(self, product_id: str) -> None:
        """Display a dummy receipt."""
        product = PRODUCTS.get(product_id)
        if product:
            st.markdown(f"""
            ### Receipt
            **Plan:** {product['name']}
            **Amount:** ${product['price']}
            **Period:** Per {product['period']}
            **Date:** {datetime.now().strftime('%Y-%m-%d')}
            **Status:** Paid
            """)
            st.markdown("---")
            st.markdown("_This is a demo receipt. In production, you would receive an actual receipt from Stripe._") 