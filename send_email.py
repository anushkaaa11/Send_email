from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)



@app.route('/send_email', methods=['POST'])
def send_email():
    # Get data from the request
    data = request.json
    subject = data.get('subject')
    message = data.get('message')

    # Email configuration
    email = "anushkaranjan141113@gmail.com"
    receiver_email = "ranjananushka29@gmail.com"
    password = "nfxv pmgj zqcp udwj"  # You should use environment variables for sensitive data

    # Validate input
    if not subject or not message:
        return jsonify({'error': 'Subject and message are required'}), 400

    try:
        # Create the email message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = receiver_email

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email, password)
            server.send_message(msg)

        return jsonify({'message': f'Email has been sent to {receiver_email}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)