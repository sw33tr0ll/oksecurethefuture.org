import json

def donate(event, _):
    html_page = """
    <html>
        <head>
            <title>OK Secure the Future</title>
        </head>
        <body>
            <h3>Coming soon...</h3>
            <p>Ask Logan for Scholarships</p>
        </body>
    </html>
    """
    http_response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": html_page
    }
    return http_response