<p align="center">
  <img width="879" alt="スクリーンショット 2023-06-06 23 23 25" src="https://github.com/EIKINAKAYAMA/git-contributions-cheater/assets/65437818/164f75d8-bc13-4ef0-a89b-e5841b08edc7">
</p>
<p align="center">
    <em>GitHub contributions cheater, Manipulate your inteview and change your feature</em>
</p>
<p align="center">
   <a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
      <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
   </a>
   <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" target="_blank">
      <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" alt="Coverage">
   </a>
   <a href="https://pypi.org/project/fastapi" target="_blank">
      <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
   </a>
</p>

---
[![issue](https://camo.githubusercontent.com/69130ab98f3c78a3c04a36832896b07da8581732262041d0f95f700e7f3b9709/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e6865726f6b756170702e636f6d2f62616467652f49737375652d7265642e7376673f6c6f676f3d69737375652d6f70656e6564266c6f676f436f6c6f723d666666)]()
[![fork](https://camo.githubusercontent.com/d9fce1c19fadb9189ab606df2e15f5c38f5e09969651511a09033d9a58bda4a6/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e6865726f6b756170702e636f6d2f62616467652f466f726b2d6f72616e67652e7376673f6c6f676f3d666f726b)]()
[![star](https://camo.githubusercontent.com/b1b58f67f9a05609086e50c816eafc4a5db9c3e3f7f35cd7d9353984ecb8b74c/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e6865726f6b756170702e636f6d2f62616467652f537461722d79656c6c6f772e7376673f6c6f676f3d73746172)]()
[![commit](https://camo.githubusercontent.com/2895770ffcfae76d05c914ad42a3fe2274d2fae509d3a28fcd86ec800d694287/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e6865726f6b756170702e636f6d2f62616467652f436f6d6d69742d677265656e2e7376673f6c6f676f3d6769742d636f6d6d6974266c6f676f436f6c6f723d666666)]()
[![repo](https://camo.githubusercontent.com/b607c0ac7a6e4540bf5f6af181391ff51c1fe6f1e950a2630b4fbf5a43969aa7/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e6865726f6b756170702e636f6d2f62616467652f5265706f2d626c75652e7376673f6c6f676f3d7265706f)]()
[![pull-request](https://camo.githubusercontent.com/cc286c7fbb8d423b9bae145d7231fc6b6490c2925d1868ba8b04fb4f27398d8a/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e6865726f6b756170702e636f6d2f62616467652f50756c6c253230526571756573742d707572706c652e7376673f6c6f676f3d7072)]()

[![Github](https://img.shields.io/badge/--FFFFFF?style=social&logo=github&label=Follow%20EIKINAKAYAMA)](https://github.com/EIKINAKAYAMA)
[![Twitter](https://img.shields.io/badge/--FFFFFF?style=social&logo=twitter&label=Follow%20EIKINAKAYAMA)](https://twitter.com/@eiki111ixa)

### Before :neutral_face: :no_mouth: :unamused: 
![スクリーンショット 2023-06-07 15 33 10](https://github.com/EIKINAKAYAMA/git-contributions-cheater/assets/65437818/ad26a0fe-13d4-4358-bd18-5720c5125dc0)
### After :muscle: :relieved: :heart: :sunglasses: :metal: :wink: :fire: :dancer: :fireworks: :tada:
![スクリーンショット 2023-06-07 15 35 58](https://github.com/EIKINAKAYAMA/git-contributions-cheater/assets/65437818/338eb365-2aa1-4879-bad4-21492e1ee85a)
# How it works
The contribution.py script initializes an empty git repository, creates a text file and starts generating changes to the file **according to "data.json"**.

There is a sample.json in data folder, so you can customize "data.json" whatever you want, also **the dataByAnswer.py supports creating your own data.json**, just answering a few quetions.

Once the commits are generated it links the created repository with
the remote repository and pushes the changes.

- [Example](https://github.com/EIKINAKAYAMA/example-git-contributions-cheater)


# Usage -contribution.py-

1. Create an empty GitHub repository. Do not initialize it.
2. Download [this repo](https://github.com/EIKINAKAYAMA/git-contributions-cheater/archive/main.zip) and unzip.
3. Setting "data.json"  ([Usage -dataByAnswer.py-](#Usage-dataByAnswer.py-))
4. Run following command.
```sh
python contribute.py --repository=git@github.com:${user}/${repo}.git
```
ex.
```sh
ex:python contribute.py --repo_path=git@github.com:EIKINAKAYAMA/example-git-contributions-cheater.git
```
Then you have a repository with lots of changes in your GitHub account.
Note: It might takes several minutes for GitHub to reindex your activity.


# Usage -dataByAnswer.py-

1.  Run following command.
```sh
python data/dataByAnswer.py
```
2. There are several questions for getting preferences of your contributions, please refer following and answer it.

- Contribution Date setting Logic

![スクリーンショット 2023-06-07 0 44 34](https://github.com/EIKINAKAYAMA/git-contributions-cheater/assets/65437818/605febfd-c39b-4127-8f82-6db1ff6a4e41)

- Contribution Number setting Logic
<img width="927" alt="スクリーンショット 2023-06-07 0 51 50" src="https://github.com/EIKINAKAYAMA/git-contributions-cheater/assets/65437818/f8f18000-53db-4f8f-b1b3-c5e89bfdc61e">


## Making contributions private
Note: This script doesn't encourage you to cheat. Cheating is bad. But if anybody
is judging your professional skills by the graph at your GitHub profile (which
caries no value) they deserve to see a rich graph.

For that matter, you might want to make the generated repository private. It is free
on GitHub. Now, you only need to set up your account 
[to show private contributions](https://help.github.com/en/articles/publicizing-or-hiding-your-private-contributions-on-your-profile).
This way GitHub users will see that you contributed something, but they won't be
able to see what exactly.

## License

[Apache License 2.0](LICENSE)
