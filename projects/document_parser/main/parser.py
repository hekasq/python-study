import datetime


def for_test():
    return 1


def parse():
    results = {}
    beginning = None
    first_timestamp = None
    min_length = None
    max_length = None
    dropped = 0
    with open('timestamps', mode='r') as ts_file:
        for line in ts_file:
            content = line[:-1].split("|")
            cid = content[2]
            timestamp = content[0]
            if first_timestamp is None:
                beginning = datetime.datetime.fromtimestamp(int(timestamp))
                first_timestamp = timestamp
            if cid in results:
                result_list = results[cid]
                total_length = f'{float((int(timestamp) - int(result_list[1])) / 3600):.2f}'
                result_list.append(timestamp)
                result_list.append(total_length)
                dropped = dropped + 1
                if min_length is None:
                    min_length = total_length
                    max_length = total_length
                if float(total_length) > float(max_length):
                    max_length = total_length
                if float(total_length) < float(min_length):
                    min_length = total_length

                result_list.append(content[3])
            else:
                results[cid] = [cid, timestamp]

    with open('outputs.csv', mode='w+') as output:
        output.write('cid, beginning, end, hours_connected, status_code\n')
        for key in results.keys():
            output.write(','.join(str(e) for e in results[key]))
            output.write('\n')

        output.write('Beginning ')
        output.write(str(beginning))
        output.write('\n')
        output.write('End =')
        output.write(str(datetime.datetime.now()))
        output.write('\n')
        output.write('Min =')
        output.write(min_length)
        output.write('\n')
        output.write('Max =')
        output.write(max_length)
        output.write('\n')
        output.write('Total = ')
        output.write(str(len(results)))
        output.write('\n')
        output.write('Dropped= ')
        output.write(str(dropped))


if __name__ == '__main__':
    parse()
