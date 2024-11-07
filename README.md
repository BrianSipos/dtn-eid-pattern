# Bundle Protocol Endpoint ID Patterns

The internet-draft is hosted at [draft-ietf-dtn-eid-pattern](https://datatracker.ietf.org/doc/draft-ietf-dtn-eid-pattern/).

A local build of the current main branch is available [draft-ietf-dtn-eid-pattern.html](https://briansipos.github.io/dtn-eid-pattern/draft-ietf-dtn-eid-pattern.html) with its [misspelling.txt](https://briansipos.github.io/dtn-eid-pattern/misspelling.txt).
A difference from the datatracker draft and this local version can be [viewed side-by-side](https://author-tools.ietf.org/diff?doc_1=draft-ietf-dtn-eid-pattern&url_2=https://briansipos.github.io/dtn-eid-pattern/draft-ietf-dtn-eid-pattern.txt&raw=1).

Prerequisites to building can be installed on Ubuntu with:
```
sudo apt-get install -y cmake python3 python3-pip python3-setuptools python3-wheel ruby xmlstarlet aspell
pip3 install xml2rfc abnf
crate install cddl
```
and update the user's path similar to
```
export PATH="${PATH}:$HOME/.cargo/bin
```

and then the document can be built with
```
cmake -S . -B build/default
cmake --build build/default
```
