
# 🎫 Customer Support Ticket Agent

An AI-powered Customer Support Ticket Agent that automatically analyzes customer support tickets, categorizes issues, assigns priority levels, and generates suggested responses. This project demonstrates an Agentic AI workflow where the system makes decisions based on the content of customer queries.


## 📌 Features

* 📂 Upload or enter customer support tickets
* 🤖 AI-powered ticket analysis
* 🏷️ Automatic issue categorization
* ⚡ Priority detection (Low, Medium, High)
* 💡 Suggested resolution for customer issues
* 📊 Displays structured ticket analysis
* 🖥️ Simple and interactive Streamlit interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* Python-dotenv
* Pandas

## 📁 Project Structure

```text
Customer_Support_Ticket_Agent/
│── app.py
│── requirements.txt
│── .env
│── README.md
│── utils.py
│── prompts.py
└── assets/
```


## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Customer_Support_Ticket_Agent.git
```

### 2. Navigate to the Project Folder

```bash
cd Customer_Support_Ticket_Agent
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file and add your Google Gemini API key:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 5. Run the Application

```bash
streamlit run app.py
```

## 🚀 How It Works

1. Enter or upload a customer support ticket.
2. The AI agent analyzes the ticket.
3. It identifies the issue category.
4. Assigns a priority level.
5. Generates a suggested response or solution.
6. Displays the complete analysis in an easy-to-read format.

## 📷 Sample Workflow

```text
Customer Ticket
        │
        ▼
AI Analysis
        │
        ▼
Issue Categorization
        │
        ▼
Priority Detection
        │
        ▼
Suggested Resolution
        │
        ▼
Display Results


## 📌 Example Categories

* Billing Issues
* Technical Support
* Account Management
* Login Problems
* Refund Requests
* Product Inquiry
* Feature Request
* Complaint
* General Query

---

## 🎯 Future Enhancements

* Multi-language support
* Email integration
* Ticket history management
* Dashboard with analytics
* Automatic ticket assignment to support teams
* PDF report generation

## 🤝 Contributing

Contributions are welcome. Feel free to fork this repository, improve the project, and submit a pull request.


## 📄 License

This project is developed for educational and learning purposes.


## 👨‍💻 Author

**GARIKINI DIVAKAR**

GitHub: https://github.com/your-username

