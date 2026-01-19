from cryptography import x509 # type: ignore
from cryptography.x509.oid import NameOID # type: ignore
from cryptography.hazmat.primitives import hashes, serialization # type: ignore
from cryptography.hazmat.primitives.asymmetric import rsa # type: ignore
from cryptography.hazmat.backends import default_backend # type: ignore
from datetime import datetime, timedelta, timezone

# Generate key pair
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Buat subject & issuer (self-signed certificate)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, "example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(timezone.utc))
    .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
    .sign(
        private_key=key,
        algorithm=hashes.SHA256(),
        backend=default_backend()
    )
)

# Simpan private key
with open("private_key.pem", "wb") as f:
    f.write(
        key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat:")
print("- private_key.pem")
print("- cert.pem")
