# Notes

Install:

1. Set up wireguard.
2. Download k3s install script from website.
3. For master:
   `./k3s.sh`
4. For node:
   `curl -sfL https://get.k3s.io | K3S_URL=https://myserver:6443 K3S_TOKEN=mynodetoken sh -`
   "The value to use for K3S_TOKEN is stored at /var/lib/rancher/k3s/server/node-token"
5. Install kubectl on laptop.
6. Copy `/etc/rancher/k3s/k3s.yaml` to laptop and change localhost IP to wireguard IP.
7. `kubectl cluster-info`
8. Install tkn CLI.
   `https://tekton.dev/docs/cli/`
   I installed manually.
4. Apply dns updates and rollout restart of codedns:
   `kubectl rollout restart -n kube-system deployment/coredns`

Install Tekton:
```
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
kubectl apply --filename https://storage.googleapis.com/tekton-releases/triggers/latest/release.yaml
kubectl apply --filename https://storage.googleapis.com/tekton-releases/triggers/latest/interceptors.yaml
```
Set up local registry on master.
(I didn't document this process.)

Tell k3s about it:
```sudo vim /etc/rancher/k3s/registries.yaml```
```
configs:
  "192.168.1.128:8443":
    auth:
      username: k3s
      password: password
    tls:
      ca_file: /home/jimmy/registry/certs/domain.crt

```
Restart k3s.

Apply rest of the CRDs.


# Bad Ideas

Amabassador: (for knative)

Start with these instruction to disable traefik.
https://www.suse.com/c/rancher_blog/deploy-an-ingress-controller-on-k3s/
use `--disable=traefik` in systemd.
The equal is important...

Follow the instructions https://www.getambassador.io/docs/edge-stack/latest/topics/install/yaml-install/ to install ambassador.

I used the file in ./ambassador/listener.yaml to set up the listener.

I'm not sure why ambassdor is listening on 80 instead of 8080 given the
settings I applied, or why changing from 8080 to 80 in the seeting borks
it.

I removed amabassador andput back traefik.


Set up Tekton Dashboard:
```
kubectl apply --filename https://storage.googleapis.com/tekton-releases/dashboard/latest/tekton-dashboard-release.yaml
```
Port forward locally:
```
kubectl port-forward -n tekton-pipelines service/tekton-dashboard 9097:9097
```

If we later want to do this on an overlay network:
3. For master:
   `INSTALL_K3S_EXEC="server --node-ip '10.100.100.5' --advertise-address '10.100.100.5' --flannel-iface 'wg0'" ./k3s.sh`
4. For node:
   `INSTALL_K3S_EXEC="agent --server 'https://10.100.100.5:6443' --token 'K3S_TOKEN' --node-ip '10.100.100.?' --advertise-address '10.100.100.?' --flannel-iface 'wg0'" ./k3s.sh`
For now sticking to single node...

Set up a namespace:
```
kubectl create -f j7s-dev-namspace.json
```
```
kubectl config set-context j7s-dev --namespace=j7s-dev \
  --cluster=j7s-dev \
  --user=default
```
I'm not sure the above command works...
