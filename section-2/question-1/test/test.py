import polars as pl
import pathlib


def get_dataframe(path: str) -> pl.DataFrame:
    path = pathlib.Path(path)
    return pl.read_csv(path)


def transform_dataframe(df: pl.DataFrame) -> pl.DataFrame:
    query = """
        select a.*
        from (
            select
                customer_id,
                sum(amount) as total_purchase
            from
                orders
            group by
                customer_id
        ) a
        order by a.total_purchase desc
        limit 5
    """

    return df.sql(query, table_name="orders")


if __name__ == "__main__":
    df = get_dataframe("section-2/question-1/test/infos.csv")
    df_transformed = transform_dataframe(df)
    print(df_transformed)
