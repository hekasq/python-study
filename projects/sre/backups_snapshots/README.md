Alright, let's adapt the previous task to focus on Google Cloud Platform (GCP) using its Python client libraries. This task will involve automating snapshot management for persistent disks in GCP environments, which is a crucial aspect for data backup and recovery in cloud infrastructure.

### Task Description: Automate Snapshot Management for GCP Persistent Disks

#### Background:
Persistent disks in GCP can be used for various applications like databases, file storage, and virtual machine instances. Regularly creating snapshots of these disks ensures data is backed up and can be crucial for disaster recovery.

#### Objective:
Write a Python script that automates the management of snapshots for GCP persistent disks. The script should:
1. List all disks in a project based on specific labels (e.g., `backup: true`).
2. Create snapshots for these labeled disks.
3. Enforce a retention policy by deleting snapshots that are older than a specified period (e.g., 7 days).

#### Requirements:
- Use Google Cloud Client Library for Python (`google-cloud-compute`).
- The script should interact with GCP's Compute Engine to manage snapshots.
- Include error handling for common issues like API limits or network errors.
- Make the script configurable via command-line arguments or a configuration file for parameters like GCP project ID, disk labels, retention period, etc.

#### Steps to Complete the Task:

1. **Setup Environment**:
   - Install Python 3 and `google-cloud-compute`.
   - Set up GCP authentication (using service account keys or default application credentials).

2. **Script Outline**:
   - **Initialization**: Initialize GCP Compute Engine client and parse configuration or command-line arguments.
   - **Disk Listing**: Query all disks in the specified project with the label indicating they require backups.
   - **Snapshot Creation**: For each disk, initiate a snapshot creation, tagging the snapshot with creation date and disk ID for easier management.
   - **Snapshot Retention**: List all snapshots for disks and delete those that exceed the retention period.

3. **Testing**:
   - Test the script in a non-production environment to ensure it correctly lists disks, creates snapshots, and deletes old snapshots.
   - Validate that the script handles errors gracefully and logs appropriate messages.

4. **Documentation**:
   - Provide detailed comments within the script for clarity.
   - Write a README.md that includes instructions on installation, configuration, and execution of the script.

#### Advanced (Optional):
- Enhance the script to handle multiple GCP regions.
- Add notifications via email or Google Cloud Pub/Sub when actions are performed or if errors occur.

This task is designed to offer hands-on experience with GCP's compute services and Python automation scripting, addressing key SRE responsibilities like proactive monitoring and disaster recovery.