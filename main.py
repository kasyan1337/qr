import qrcode
import datetime
import os
import base64

# === Ensure 'output' folder exists ===
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Create the output folder if it doesn't exist

# === CUSTOMIZABLE CONTACT DETAILS ===
first_name = "Kasim"
last_name = "Janči"
title = "MPhil."
formatted_name = f"{title} {first_name} {last_name}"

company = "Welding & Testing of Materials s.r.o."
job_title = "Procurement Manager"

phone_work = "+421 944 118 730"
phone_mobile = "+421 944 118 730"
phone_home = "+421 944 118 730"
phone_fax = "+421 944 118 730"

email_work = "kjanci@wtm.sk"
email_personal = "kasim.janci@gmail.com"

website = "https://www.wtm.sk"
linkedin = "https://www.linkedin.com/in/kasimjanci"
twitter = "https://twitter.com/kasim"

street = "Dlhá 1011/88D"
city = "Žilina"
region = ""  # Optional
postal_code = "01009"
country = "Slovakia"

birthday = "1998-10-08"  # YYYY-MM-DD format
profile_picture_path = "images/photo_sjtu.png"  # Ensure this file is small

notes = "Experienced procurement specialist in welding and materials testing."

# === EMBED IMAGE INTO VCARD ===
def encode_image_to_base64(image_path):
    """Encodes an image as a Base64 string for embedding in a vCard."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print("⚠️ Profile picture not found. Skipping image embedding.")
        return None

# Convert image to Base64 (Ensure the image is resized beforehand)
profile_picture_base64 = encode_image_to_base64(profile_picture_path)

# === GENERATE vCard FORMAT (Optimized to reduce size) ===
vcard_data = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;{title};
FN:{formatted_name}
ORG:{company}
TITLE:{job_title}
TEL;WORK:{phone_work}
TEL;CELL:{phone_mobile}
TEL;HOME:{phone_home}
TEL;FAX:{phone_fax}
EMAIL;WORK:{email_work}
EMAIL;HOME:{email_personal}
URL:{website}
URL;LinkedIn:{linkedin}
URL;Twitter:{twitter}
ADR;WORK:;;{street};{city};{region};{postal_code};{country}
BDAY:{birthday}
NOTE:{notes}
"""

# Add image only if available
if profile_picture_base64:
    vcard_data += f"PHOTO;ENCODING=b;TYPE=JPEG:{profile_picture_base64}\n"

vcard_data += "END:VCARD"

# === GENERATE QR CODE (Manually specify a large version and optimize) ===
qr = qrcode.QRCode(
    version=40,  # Increase version to support large data (max 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Reduce error correction for more data
    box_size=10,  # Increase box size for better readability
    border=4,  # Standard border size
)

qr.add_data(vcard_data)
qr.make(fit=True)  # Adjusts size dynamically

# Create a timestamped filename (Fix: No slashes `/` in filename)
now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
vcard_filename = f"{first_name}_{last_name}_{now}.png"

# Save the QR code inside the 'output' folder
output_path = os.path.join(output_folder, vcard_filename)
img = qr.make_image(fill="black", back_color="white")
img.save(output_path)

print(f"✅ QR Code generated and saved at: {output_path}")