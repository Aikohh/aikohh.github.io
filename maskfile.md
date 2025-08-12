# Tasks
Development tasks for this mkdocs project

## activate
> Activate nix development shell for all project dependencies

```sh
nix-shell
```

## serve
> Build the site and host it on a local webserver with live preview

```sh
mkdocs serve
```

## build
> Build the site for deployment

```sh
mkdocs build
```

## Convert video to small webm
> Example command for converting an mp4 into a webm with a width of 1024 px, 24 fps, and high compression

```sh
ffmpeg -i FamiliarHarmony.mp4 -c:v libsvtav1 -crf 45 -preset 6 -vf "scale=1024:-1,fps=24" -an FamiliarHarmony.webm
```
