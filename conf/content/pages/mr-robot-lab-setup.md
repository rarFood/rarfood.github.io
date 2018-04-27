Title: Mr Robot Lab Setup
Slug: mr-robot-lab-setup


## Shopping List:
 >Note: Your Host Machine needs to be able to run virtual machines

  1. [VirtualBox](https://www.virtualbox.com/wiki/Downloads)
  2. [VirtualBox Extensions pack](https://download.virtualbox.org/virtualbox/5.2.10/Oracle_VM_VirtualBox_Extension_Pack-5.2.10.vbox-extpack)
  3. [Mr-Robot:1 Virtual Machine](https://www.vulnhub.com/entry/mr-robot-1,151/)
  4. [Kali Linux Virtual Machine](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-hyperv-image-download/)

## VirtualBox Setup:
  1. After downloading [VirtualBox](https://www.virtualbox.com/wiki/Downloads) and installing the [extensions pack](https://download.virtualbox.org/virtualbox/5.2.10/Oracle_VM_VirtualBox_Extension_Pack-5.2.10.vbox-extpack) you should create a new natnetwork so that the vms that we are going to use can comunicate with each other.

    ![Natnetwork setup 1](../images/virtualBoxPreferences.png)

    ![Natnetwork setup 2](../images/virtualBoxNetworks.png)

    ![Natnetwork setup 3](../images/virtualboxCreateNatnetwork.png)

## VM Setup:
  1. After downloading the vms just double click on them and [VirtualBox](https://www.virtualbox.com/wiki/Downloads) should open asking if you want to import the vms.
    * picture

  2. Modify if you need to (i add more ram to the kali linux vm) and click import
    * pictures

## Finishing Touches:
  1. [Go to the tutorial](http://bacalaitopentester.com/pdfs/mrR0b0+.pdf) and try to do the challenges. Good luck !

  > With love Daniel San...
