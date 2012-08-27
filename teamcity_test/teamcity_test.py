from pkg_resources import EntryPoint
from teamcity.unittestpy import TeamcityTestRunner, TeamcityTestResult
from setuptools.command.test import test

class ExtendedTeamcityTestRunner(TeamcityTestRunner):
    def _makeResult(self):
        return ExtendedTeamcityResult(self.stream)


class ExtendedTeamcityResult(TeamcityTestResult):

    def startTest(self, test):
        self.testsRun += 1
        TeamcityTestResult.startTest(self, test)

    def printResults(self):
        self.output.write('\nTests run: %i, Failures: %i, Errors %i \n\n' % (self.testsRun, len(self.failures), len(self.errors)))
        self._print_test_names_of_list_as(self.failures, 'Failures')
        self._print_test_names_of_list_as(self.errors, 'Errors')

    def _print_test_names_of_list_as(self, tests, label):
        if len(tests) > 0:
            self.output.write('%s:\n' % label)
            for failure in tests:
                self.output.write('\t%s\n' % self.getTestName(failure[0]))
            self.output.write('\n\n')


class teamcity_test(test):

    def run_tests(self):
        import unittest
        loader_ep = EntryPoint.parse("x="+self.test_loader)
        loader_class = loader_ep.load(require=False)
        unittest.main(
            None, None, [unittest.__file__]+self.test_args,
            testLoader = loader_class(),
            testRunner = ExtendedTeamcityTestRunner()
        )


