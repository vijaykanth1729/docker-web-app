node {
  checkout scm
  docker.withRegistry('https://587354497551.dkr.ecr.us-east-1.amazonaws.com','ecr:us-east-1:myAws') {
  def customImage = docker.build("demo")
  customImage.push()
  }
}
