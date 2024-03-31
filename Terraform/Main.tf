terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.22.0"
    }
  }
}
provider "google" {
  project = "praxis-wall-411617"
  region  = "europe-west2"
  zone    = "europe-west2-b"
}

resource "google_compute_instance" "vm_instance" {
  name         = "jm-final-project"
  machine_type = "e2-standard-4"

  boot_disk {
    initialize_params {
      image = "ubuntu-2004-focal-v20240229"
      size = "60"
    }
  }
  
  network_interface {
    # A default network is created for all GCP projects
    network = google_compute_network.vpc_network.self_link
    access_config {
    }
  }
}

resource "google_compute_network" "vpc_network" {
  name                    = "terraform-network"
  auto_create_subnetworks = "true"
}

resource "google_storage_bucket" "data-lake-bucket" {
  name                        = "jm-data-lake"
  location                    = "EU"
  force_destroy               = true
  uniform_bucket_level_access = true
}

