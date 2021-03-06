import os,sys,yaml,subprocess

class Packager(object):
    def __init__(self, box):
        self.params = yaml.load(open('./metadata/%s.yml' % box).read())

    def package(self):
        self._move_old_package()
        ret_value = self._run_package_command()
        print 'ret_value:', ret_value
        if not ret_value:
            self._bump_box_version()
        self._save_yaml()

    def _move_old_package(self):
        if os.path.exists('./boxes/%s.box' % self.params.get('name')):
            os.rename('./boxes/%s.box' % self.params.get('name'), './boxes/%s_%d.box' % (self.params.get('name'), self.params.get('version')))

    def _run_package_command(self):
        return subprocess.call(['vagrant', 'package', '--base', self.params.get('base'), '--output', './boxes/%s.box' % self.params.get('name')])

    def _bump_box_version(self):
        self.params['version'] += 1

    def _save_yaml(self):
        with open('./metadata/%s.yml' % self.params.get('name'), 'w') as yml:
            yml.write(yaml.dump(self.params, default_flow_style=False))

if __name__=='__main__':
    pack = Packager(sys.argv[1])
    pack.package()
