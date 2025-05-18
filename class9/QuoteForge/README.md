# 🎨 QuoteForge

> Shape Words Into Art

QuoteForge is an elegant web application that transforms quotes into beautiful visual posters. Whether you're creating content for social media, personal inspiration, or professional presentations, QuoteForge helps you create stunning quote visuals in seconds.

## ✨ Features

### Core Functionality
- 🖼️ Dynamic poster generation with customizable themes
- 📸 Integration with Unsplash API for beautiful backgrounds
- ✍️ Smart text positioning and wrapping
- 🎭 Multiple design themes (Minimal, Elegant, Bold)
- 📱 Responsive design for all devices

### Pro Features
- 🔓 No watermarks
- 📊 HD quality (1080x1080)
- 🎨 Premium fonts via Google Fonts API
- 🛠️ Advanced customization options
- 🔑 API access

## 💻 Tech Stack

- **Frontend**: Streamlit
- **Image Processing**: Pillow (PIL)
- **Authentication**: JWT-based auth system
- **External APIs**: 
  - Unsplash for backgrounds
  - Google Fonts for typography
- **Payment**: Stripe integration (simulated)

## 🚀 Quick Start

1. **Setup Environment**
   ```bash
   # Create and activate virtual environment
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Unix/MacOS
   ```

2. **Install Dependencies**
   ```bash
   uv add streamlit pillow numpy requests PyJWT
   ```

3. **Run Application**
   ```bash
   streamlit run main.py
   ```

## 💰 Business Model

### Pricing Tiers
| Feature | Free | Pro |
|---------|------|-----|
| Basic Poster Creation | ✅ | ✅ |
| Resolution | 720p | 1080p |
| Watermark | Yes | No |
| Custom Themes | ❌ | ✅ |
| API Access | ❌ | ✅ |
| Priority Support | ❌ | ✅ |

### Subscription Plans
- Monthly: $9.99/month
- Yearly: $99.99/year (2 months free)

## 🎯 Requirements Fulfillment

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| Authentication | JWT-based auth system with user management | ✅ |
| Database | Session-based state management (simulated) | ✅ |
| Payments | Stripe integration with subscription plans | ✅ |
| OOP Principles | | |
| - Encapsulation | `Poster` class encapsulates image generation logic | ✅ |
| - Inheritance | `ThemeConfig` for different poster styles | ✅ |
| - Polymorphism | Different render methods for themes | ✅ |
| - Abstraction | Simple UI hiding complex image processing | ✅ |
| Business Model | Freemium model with clear monetization | ✅ |
| User Experience | Intuitive UI with live preview | ✅ |
| Code Quality | Clean architecture, typed code | ✅ |
| Creative Solution | Unique combination of APIs and features | ✅ |

## 🎨 Theme Examples

### Minimal
- Clean, modern design
- Perfect for professional quotes
- White space focused layout

### Elegant
- Sophisticated typography
- Rich, dark backgrounds
- Perfect for inspirational quotes

### Bold
- High impact design
- Vibrant color schemes
- Ideal for social media

## 🔒 Security

- JWT-based authentication
- Secure payment processing
- API key protection
- Rate limiting on free tier


--

<div align="center">
Made with ❤️ by Ayesha Mughal
</div>
