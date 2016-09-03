# systemd-minecraft
This is a way to run and deploy minecraft on a systemd server
## How-to build rpm
1. git clone
```bash
git clone https://github.com/Jmainguy/systemd-minecraft
```
2. Take a tar.gz of this entire dir
```bash
tar czvf systemd-minecraft.tar.gz systemd-minecraft/*
```
3. Copy .tar.gz and .spec to rpmbuild/SOURCE and rpmbuild/SPEC and run rpmbuild

## How-to deploy rpm
1. Upload new rpm to pulp
2. Change version in group_var/all to match newly built rpm
3. Change hosts file to servers you wish to deploy to
4. Run ansible-playbook 
```bash
ansible-playbook -i hosts site.yml
```
5. Profit
