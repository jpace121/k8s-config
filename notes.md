# Notes

Install:

1. Set up wireguard.
2. Download k3s install script from website.
3. For master:
   `INSTALL_K3S_EXEC="server --node-ip '10.100.100.5' --advertise-address '10.100.100.5' --flannel-iface 'wg0'" ./k3s.sh`
4. For node:
   `INSTALL_K3S_EXEC="agent --server 'https://10.100.100.5:6443' --token 'K3S_TOKEN' --node-ip '10.100.100.?' --advertise-address '10.100.100.?' --flannel-iface 'wg0'" ./k3s.sh`
5. Install kubectl on laptop.
6. Copy `/etc/rancher/k3s/k3s.yaml` to laptop and change localhost IP to wireguard IP.
7. `kubectl cluster-info`
8. Install tkn CLI.
   `https://tekton.dev/docs/cli/`
   I installed manually.

Set up Tekton:
```
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
```
Set up Tekton Dashboard:
```
kubectl apply --filename https://storage.googleapis.com/tekton-releases/dashboard/latest/tekton-dashboard-release.yaml
```
Port forward locally:
```
kubectl port-forward -n tekton-pipelines service/tekton-dashboard 9097:9097
```

Set up a namespace:
```
kubectl create -f j7s-dev-namspace.json
```
```
kubectl config set-context j7s-dev --namespace=j7s-dev \
  --cluster=j7s-dev \
  --user=default
```

Stuff I installed from tkn.
```
tkn hub install task git-clone
tkn hub install task ansible-runner
tkn hub install task git-batch-merge
```


