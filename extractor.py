from bs4 import BeautifulSoup

class Extractor(object):
    def __init__(self, table):
        self.table = table
        self.output = []

    def parse(self):
        row_ind = 0
        col_ind = 0
        for row in self.table.find_all('tr'):
            # record the smallest row_span, so that we know how many rows
            # we should skip
            smallest_row_span = 1

            for cell in row.children:
                if cell.name in ('td', 'th'):
                    # check multiple rows
                    row_span = int(cell.rowspan) if cell.rowspan else 1
                    
                    # try updating smallest_row_span
                    smallest_row_span = min(smallest_row_span, row_span)
                    
                    # check multiple columns
                    col_span = int(cell.colspan) if cell.colspan else 1
                    
                    # find the right index
                    while True:
                        if self.check_validity(row_ind, col_ind, row_span, col_span):
                            break
                        col_ind += 1

                    # insert into self.output
                    self.insert(row_ind, col_ind, row_span, col_span)

                    # update col_ind
                    col_ind += col_span

            # update row_ind
            row_ind += smallest_row_span

    def print(self):
        return self.output


    def check_validity(self, i, j, height, width):
        """
        check if a rectangle (i, j, height, width) can be put into self.output
        """
        return all(self.check_cell_validity(ii, jj) for ii in range(i, i+height) for jj in range(j, j+width))

    def check_cell_validity(self, i, j):
        """
        check if a cell (i, j) can be put into self.output
        """
        if i >= len(self.output):
            return True
        if j >= len(self.output[i]):
            return True
        if self.output[i][j] is None:
            return True
        return False

    def insert(self, i, j, height, width, val):
        for ii in range(i, i+height):
            for jj in range(j, j+width):
                self.insert_cell(ii, jj, val)

    def insert_cell(self, i, j, val):
        while i >= len(self.output):
            self.output.append([])
        while j >= len(self.output[i]):
            self.output.append(None)

        self.output[i][j] = val