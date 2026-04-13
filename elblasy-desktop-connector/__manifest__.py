{
    "name": "Elblasy Desktop Connector",
    "version": "1.0",
    "depends": ["base", "base_setup", "sale_management", "stock", "purchase"],
    "author": "elblasy.app",
    "category": "Tools",
    "website": "https://elblasy.app/",
    "license": "LGPL-3",
    "summary": "Desktop Connection Settings",
    "description": """
Elblasy Desktop Connector transforms your Odoo experience into a powerful desktop-like application with advanced price checking capabilities.

This innovative module allows you to use Odoo as if it were a native desktop application through advanced web desktop technology. It provides a comprehensive price checker application that connects seamlessly with your Odoo system, featuring intelligent background responsiveness that adapts to product colors for enhanced visual experience and brand consistency.

Perfect for retail environments, this solution enables customers to easily discover product prices through an intuitive interface that maintains your brand identity. The application integrates flawlessly with existing Odoo workflows, providing real-time access to product information, pricing, and inventory data.

Key Features:
• Desktop-like Odoo experience with native app feel
• Advanced price checker application with real-time data
• Intelligent color-responsive backgrounds that adapt to product themes
• Retail-optimized interface for customer self-service
• Seamless Odoo ERP integration with full data synchronization
• Customizable settings for different retail environments
• Mobile-responsive design for various screen sizes
• Real-time inventory and pricing updates

Installation and Setup:
1. Install the module from the Odoo Apps page
2. Configure desktop connection settings in your preferences
3. Access the desktop-like interface through the main menu
4. Customize the price checker for your retail environment
5. Configure product color mappings for background responsiveness

This module is ideal for retail stores, supermarkets, electronics shops, and any business that needs to provide customers with easy access to product pricing information while maintaining a professional, branded experience.

For technical support and customization services, visit our website at https://elblasy.app/ or contact our support team.
    """,
    "images": [
        "static/description/icon.png"
    ],
    "data": [
        "views/connector_views.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}
