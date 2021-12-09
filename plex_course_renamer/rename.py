import os
import click

extensions = ('asf','avi','mov','mp4','mpeg','mpegets','ts','mkv','wmv')

@click.command()
@click.option('--dir', default='./', help='The directory of the files to rename')
def run(dir):
    path = os.path.abspath(dir)
    tree = [x for x in os.walk(path)]
    for i, f in enumerate(tree[1:]):
        counter = 0
        for z, vid in enumerate(f[2]):
            vname, ext = vid.rsplit('.',1)
            if ext not in extensions:
                continue
            else:
                counter += 1
            name = path.split("\\")[-1]

            os.rename(f'{path}\\{tree[0][1][i]}\\{vid}', f'{path}\\{tree[0][1][i]}\\{name} - s{i+1}e{counter} - {vid}')
            print(f'{path}\\{tree[0][1][i]}\\{vname}.en.srt')
            if os.path.isfile(f'{path}\\{tree[0][1][i]}\\{vname}.en.srt'):
                print('sucess')
                os.rename(f'{path}\\{tree[0][1][i]}\\{vname}.en.srt', f'{path}\\{tree[0][1][i]}\\{name} - s{i+1}e{counter} - {vname}.en.srt')


if __name__ == "__main__":
    run()