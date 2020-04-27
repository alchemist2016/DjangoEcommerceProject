import os

os.environ["SECRET_KEY"] = "ddba%l7!!g7gfc70vm3=xxqvrg%_frgt=cbqpywuq@mb&31go-"
os.environ["DEVELOPMENT"] = "1"
os.environ["HOSTNAME"] = "django-ecommerce-project-app.herokuapp.com"

os.environ.setdefault("STRIPE_PUBLISHABLE", "pk_test_UMjeQLCNbw9Q1uikQO3H557W00vLqTaw9m")
os.environ.setdefault("STRIPE_SECRET", "sk_test_XVIvVXHYroBw7WpHjtguzWhX00dmXohyQW")

os.environ.setdefault("DATABASE_URL", "postgres://iukiohsrxdcxlx:decdd6909609f5a5e9362bb5affd9060cf419614dc04c695fc9a186cc2b56595@ec2-54-247-103-43.eu-west-1.compute.amazonaws.com:5432/db5vr1b6l8psgv")
