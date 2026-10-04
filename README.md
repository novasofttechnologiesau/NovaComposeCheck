# NovaComposeCheck

Static checks for risky Docker Compose settings. Run `novacomposecheck compose.yaml`. Reports privileged containers, host networking, writable Docker socket mounts, and published database ports. It never starts containers. Findings are heuristics and need operator review.
