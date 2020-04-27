import os

os.environ["SECRET_KEY"] = "ddba%l7!!g7gfc70vm3=xxqvrg%_frgt=cbqpywuq@mb&31go-"
os.environ["DEVELOPMENT"] = "1"

os.environ.setdefault("STRIPE_PUBLISHABLE", "pk_test_UMjeQLCNbw9Q1uikQO3H557W00vLqTaw9m")
os.environ.setdefault("STRIPE_SECRET", "sk_test_XVIvVXHYroBw7WpHjtguzWhX00dmXohyQW")
