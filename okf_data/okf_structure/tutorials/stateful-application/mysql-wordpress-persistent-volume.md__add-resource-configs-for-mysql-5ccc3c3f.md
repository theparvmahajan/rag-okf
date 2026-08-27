---
id: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#add-resource-configs-for-mysql-and-wordpress
kind: section
title: Add resource configs for MySQL and WordPress
source: tutorials/stateful-application/mysql-wordpress-persistent-volume.md
url: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
heading: Add resource configs for MySQL and WordPress
parent: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume
children: []
prev_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#create-a-kustomization-yaml
next_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#apply-and-verify
word_count: 121
---

The following manifest describes a single-instance MySQL Deployment. The MySQL
container mounts the PersistentVolume at /var/lib/mysql. The `MYSQL_ROOT_PASSWORD`
environment variable sets the database password from the Secret.

The following manifest describes a single-instance WordPress Deployment. The WordPress container mounts the
PersistentVolume at `/var/www/html` for website data files. The `WORDPRESS_DB_HOST` environment variable sets
the name of the MySQL Service defined above, and WordPress will access the database by Service. The
`WORDPRESS_DB_PASSWORD` environment variable sets the database password from the Secret kustomize generated.

1. Download the MySQL deployment configuration file.

   ```shell
   curl -LO https://k8s.io/examples/application/wordpress/mysql-deployment.yaml
   ```

2. Download the WordPress configuration file.

   ```shell
   curl -LO https://k8s.io/examples/application/wordpress/wordpress-deployment.yaml
   ```

3. Add them to `kustomization.yaml` file.

   ```shell
   cat <<EOF >>./kustomization.yaml
   resources:
     - mysql-deployment.yaml
     - wordpress-deployment.yaml
   EOF
   ```
