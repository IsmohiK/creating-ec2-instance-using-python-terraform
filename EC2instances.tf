resource "aws_instance" "resourceName" {
  ami = "${var.ami-name}"
  instance_type = "${var.instance_type}"
  count="${var.desiredCapacity}"
}

output "ime" {
   value = ["${aws_instance.resourceName.*.public_ip}"]
}