terraform {
    required_providers {
      docker = {
        source  = "kreuzwerker/docker"
        version = "~> 2.21.0"
       }
    }
}

provider "docker" {}

resource "docker_image" "my_image" {
  name = "userisabdullah/devops:46"
}

resource "docker_container" "my_container" {
  name  = "NewDevops"
  image = docker_image.my_image.repo_digest

  ports {
    internal = 80
    external = 46195
  }

  # You can add environment variables or volumes if needed
  # env = [
  #   "ENV_VAR=value"
  # ]

  # volumes {
  #   container_path = "/path/in/container"
  #   host_path      = "/path/on/host"
  # }
}
